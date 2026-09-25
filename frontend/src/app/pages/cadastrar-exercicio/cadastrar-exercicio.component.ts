import {
  ChangeDetectorRef,
  Component
} from '@angular/core';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-cadastrar-exercicio',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './cadastrar-exercicio.component.html',
  styleUrl: './cadastrar-exercicio.component.css'
})
export class CadastrarExercicioComponent {
  codigoUsuario = 0;

  licoes: any[] = [];

  codigoLicao: number | null = null;
  nivelDificuldade: number | null = null;

  descricao = '';

  opcaoA = '';
  opcaoB = '';
  opcaoC = '';
  opcaoD = '';

  respostaCorreta = '';

  pontuacao = 20;

  mensagem = '';
  sucesso = false;
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

    this.carregarLicoes();
  }

  carregarLicoes() {
    this.apiService.listarLicoes().subscribe({
      next: (licoes: any) => {
        this.licoes = licoes;
        this.cdr.markForCheck();
      },

      error: () => {
        this.mensagem =
          'Não foi possível carregar as lições.';

        this.cdr.markForCheck();
      }
    });
  }

  cadastrar() {
    this.mensagem = '';
    this.sucesso = false;

    if (
      this.codigoLicao === null ||
      this.nivelDificuldade === null ||
      !this.descricao.trim() ||
      !this.opcaoA.trim() ||
      !this.opcaoB.trim() ||
      !this.opcaoC.trim() ||
      !this.opcaoD.trim() ||
      !this.respostaCorreta
    ) {
      this.mensagem =
        'Preencha todos os campos corretamente.';
      return;
    }

    this.carregando = true;

    this.apiService.cadastrarExercicio({
      codigo_licao: this.codigoLicao,
      nivel_dificuldade: this.nivelDificuldade,
      descricao: this.descricao.trim(),
      opcoes_resposta: [
        this.opcaoA.trim(),
        this.opcaoB.trim(),
        this.opcaoC.trim(),
        this.opcaoD.trim()
      ],
      resposta_correta: this.respostaCorreta.trim(),
      pontuacao: this.pontuacao
    }).subscribe({
      next: (resposta: any) => {
        this.carregando = false;
        this.sucesso = true;

        this.mensagem =
          `Exercício ${resposta.exercicio.codigo} cadastrado com sucesso.`;

        this.limparFormulario();

        this.cdr.markForCheck();
      },

      error: (erro) => {
        this.carregando = false;

        if (erro.status === 404) {
          this.mensagem =
            'Lição não encontrada.';
        } else if (erro.status === 400) {
          this.mensagem =
            erro.error?.detail ||
            'Dados do exercício inválidos.';
        } else {
          this.mensagem =
            'Não foi possível cadastrar o exercício.';
        }

        this.cdr.markForCheck();
      }
    });
  }

  limparFormulario() {
    this.codigoLicao = null;
    this.nivelDificuldade = null;

    this.descricao = '';

    this.opcaoA = '';
    this.opcaoB = '';
    this.opcaoC = '';
    this.opcaoD = '';

    this.respostaCorreta = '';

    this.pontuacao = 20;
  }

  voltar() {
    this.router.navigate([
      '/admin',
      this.codigoUsuario
    ]);
  }
}