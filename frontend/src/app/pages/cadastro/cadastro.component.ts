import {
  ChangeDetectorRef,
  Component
} from '@angular/core';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-cadastro',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './cadastro.component.html',
  styleUrl: './cadastro.component.css'
})
export class CadastroComponent {
  nome = '';
  codigoIdioma: number | null = null;

  idiomas: any[] = [];

  mensagem = '';
  carregando = false;

  constructor(
    private apiService: ApiService,
    private router: Router,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.apiService.listarIdiomas()
      .subscribe({
        next: (idiomas: any) => {
          this.idiomas = idiomas;
          this.cdr.markForCheck();
        },

        error: () => {
          this.mensagem = 'Não foi possível carregar os idiomas.';
          this.cdr.markForCheck();
        }
      });
  }

  cadastrar() {
    this.mensagem = '';

    if (
      !this.nome.trim() ||
      this.codigoIdioma === null
    ) {
      this.mensagem = 'Preencha todos os campos.';
      return;
    }

    this.carregando = true;

    this.apiService.cadastrarUsuario({
      nome: this.nome,
      codigo_idioma_aprendizado: this.codigoIdioma
    }).subscribe({
      next: (resposta: any) => {
        this.carregando = false;

        const codigo = resposta.usuario.codigo;

        alert(
          `Cadastro realizado! Seu código de usuário é: ${codigo}`
        );

        this.router.navigate([
          '/home',
          codigo
        ]);

        this.cdr.markForCheck();
      },

      error: () => {
        this.carregando = false;
        this.mensagem = 'Não foi possível realizar o cadastro.';
        this.cdr.markForCheck();
      }
    });
  }
}