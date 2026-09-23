import { ChangeDetectorRef, Component } from '@angular/core';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-cadastrar-licao',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './cadastrar-licao.component.html',
  styleUrl: './cadastrar-licao.component.css',
})
export class CadastrarLicaoComponent {
  codigoUsuario = 0;
  codigoIdioma: number | null = null;

  idiomas: any[] = [];

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

    this.carregarIdiomas();
  }

  carregarIdiomas() {
    this.apiService.listarIdiomas().subscribe({
      next: (idiomas: any) => {
        this.idiomas = idiomas;
        this.cdr.markForCheck();
      },

      error: () => {
        this.mensagem = 'Não foi possível carregar os idiomas.';
        this.cdr.markForCheck();
      },
    });
  }

  cadastrar() {
    this.mensagem = '';
    this.sucesso = false;

    if (this.codigoIdioma === null || this.codigoIdioma <= 0) {
      this.mensagem = 'Selecione um idioma.';
      return;
    }

    this.carregando = true;

    this.apiService.cadastrarLicao({codigo_idioma: this.codigoIdioma}).subscribe({
        next: (resposta: any) => {
          this.carregando = false;
          this.sucesso = true;

          this.mensagem = `Lição ${resposta.licao.codigo} cadastrada com sucesso.`;

          this.codigoIdioma = null;

          this.cdr.markForCheck();
        },

        error: (erro) => {
          this.carregando = false;

          if (erro.status === 409) {
            this.mensagem = 'Este idioma já possui uma lição cadastrada.';
          } else if (erro.status === 404) {
            this.mensagem = 'Idioma não encontrado.';
          } else {
            this.mensagem = 'Não foi possível cadastrar a lição.';
          }

          this.cdr.markForCheck();
        },
      });
  }

  voltar() {
    this.router.navigate(['/admin', this.codigoUsuario]);
  }
}
