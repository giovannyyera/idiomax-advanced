import { ChangeDetectorRef, Component } from '@angular/core';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-cadastrar-idioma',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './cadastrar-idioma.component.html',
  styleUrl: './cadastrar-idioma.component.css',
})
export class CadastrarIdiomaComponent {
  codigoUsuario = 0;

  codigoIdioma: number | null = null;
  descricao = '';

  mensagem = '';
  sucesso = false;
  carregando = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private apiService: ApiService,
    private cdr: ChangeDetectorRef,
  ) {}

  ngOnInit() {
    this.codigoUsuario = Number(this.route.snapshot.paramMap.get('codigo'));
  }

  cadastrar() {
    this.mensagem = '';
    this.sucesso = false;

    if (this.codigoIdioma === null || this.codigoIdioma <= 0 || !this.descricao.trim()) {
      this.mensagem = 'Preencha todos os campos corretamente.';
      return;
    }

    this.carregando = true;

    this.apiService
      .cadastrarIdioma({
        codigo: this.codigoIdioma,
        descricao: this.descricao.trim(),
      })
      .subscribe({
        next: () => {
          this.carregando = false;
          this.sucesso = true;
          this.mensagem = 'Idioma cadastrado com sucesso.';

          this.codigoIdioma = null;
          this.descricao = '';

          this.cdr.markForCheck();
        },

        error: (erro) => {
          this.carregando = false;

          if (erro.status === 409) {
            this.mensagem = 'Já existe um idioma com esse código.';
          } else {
            this.mensagem = 'Não foi possível cadastrar o idioma.';
          }

          this.cdr.markForCheck();
        },
      });
  }

  voltar() {
    this.router.navigate(['/admin', this.codigoUsuario]);
  }
}
