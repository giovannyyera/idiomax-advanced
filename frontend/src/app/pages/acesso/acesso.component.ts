import { Component,  ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-acesso',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './acesso.component.html',
  styleUrl: './acesso.component.css'
})
export class AcessoComponent {
  codigoUsuario: number | null = null;

  mensagem = '';
  usuarioNaoEncontrado = false;
  carregando = false;

  constructor(
    private apiService: ApiService,
    private router: Router,
    private cdr: ChangeDetectorRef
  ) {}

  buscarUsuario() {
  this.mensagem = '';
  this.usuarioNaoEncontrado = false;

  if (
    this.codigoUsuario === null ||
    this.codigoUsuario <= 0
  ) {
    this.mensagem = 'Digite um código de usuário válido.';
    return;
  }

  this.carregando = true;

  this.apiService.buscarUsuario(
    this.codigoUsuario
  ).subscribe({
    next: () => {
      this.carregando = false;

      this.cdr.markForCheck();

      this.router.navigate([
        '/home',
        this.codigoUsuario
      ]);
    },

    error: (erro) => {
      this.carregando = false;

      if (erro.status === 404) {
        this.mensagem = 'Usuário não encontrado.';
        this.usuarioNaoEncontrado = true;
      } else {
        this.mensagem = 'Não foi possível consultar o usuário.';
      }

      this.cdr.markForCheck();
    }
  });
}

  irParaCadastro() {
    this.router.navigate(['/cadastro']);
  }
}