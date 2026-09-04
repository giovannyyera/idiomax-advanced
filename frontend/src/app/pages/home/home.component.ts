import {
  ChangeDetectorRef,
  Component
} from '@angular/core';

import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';

import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    CommonModule
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  usuario: any = null;
  mensagem = '';

  codigoUsuario = 0;

  constructor(
    private route: ActivatedRoute,
    private apiService: ApiService,
    private cdr: ChangeDetectorRef,
    private router: Router
  ) {}

  ngOnInit() {
    this.codigoUsuario = Number(
      this.route.snapshot.paramMap.get('codigo')
    );

    this.apiService.buscarUsuario(
      this.codigoUsuario
    ).subscribe({
      next: (usuario) => {
        this.usuario = usuario;
        this.cdr.markForCheck();
      },

      error: () => {
        this.mensagem = 'Não foi possível carregar o usuário.';
        this.cdr.markForCheck();
      }
    });
  }

  irParaPratica() {
    this.router.navigate([
      '/pratica',
      this.codigoUsuario
    ]);
  }

  irParaRanking() {
    this.router.navigate([
        '/ranking',
        this.codigoUsuario
    ]);
  }

  irParaCertificado() {
    this.router.navigate([
      '/certificado',
      this.codigoUsuario
    ]);
  }

  excluirConta() {
    const confirmar = confirm(
      'Tem certeza que deseja excluir sua conta?'
    );

    if (!confirmar) {
      return;
    }

    this.apiService.excluirUsuario(
      this.codigoUsuario
    ).subscribe({
      next: () => {
        alert('Conta excluída com sucesso.');

        this.router.navigate(['/']);
      },

      error: () => {
        alert('Não foi possível excluir a conta.');
      }
    });
  }

  sair() {
    this.router.navigate(['/']);
  }
}