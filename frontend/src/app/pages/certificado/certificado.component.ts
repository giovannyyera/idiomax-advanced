import {
  ChangeDetectorRef,
  Component
} from '@angular/core';

import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';

import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-certificado',
  standalone: true,
  imports: [
    CommonModule
  ],
  templateUrl: './certificado.component.html',
  styleUrl: './certificado.component.css'
})
export class CertificadoComponent {
  codigoUsuario = 0;

  certificado: any = null;
  mensagem = '';
  carregando = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private apiService: ApiService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.codigoUsuario = Number(
      this.route.snapshot.paramMap.get('codigo')
    );

    this.carregarCertificado();
  }

  carregarCertificado() {
    this.carregando = true;

    this.apiService.buscarCertificado(
      this.codigoUsuario
    ).subscribe({
      next: (certificado) => {
        this.certificado = certificado;
        this.carregando = false;

        this.cdr.markForCheck();
      },

      error: (erro) => {
        this.carregando = false;

        if (erro.status === 400) {
          this.mensagem =
            'O certificado ainda não está disponível. Conclua o idioma primeiro.';
        } else {
          this.mensagem =
            'Não foi possível carregar o certificado.';
        }

        this.cdr.markForCheck();
      }
    });
  }

  abrirPdf() {
    const url =
      this.apiService.obterCertificadoPdf(
        this.codigoUsuario
      );

    window.open(url, '_blank');
  }

  voltar() {
    this.router.navigate([
      '/home',
      this.codigoUsuario
    ]);
  }
}