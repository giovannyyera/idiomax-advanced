import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-pratica',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './pratica.component.html',
  styleUrl: './pratica.component.css'
})
export class PraticaComponent implements OnInit {
  codigoUsuario = 0;
  usuario = '';
  idioma = '';
  nivelAtual = 0;
  pontuacaoTotal = 0;

  exercicios: any[] = [];
  indiceAtual = 0;
  respostaSelecionada = '';

  mensagem = '';
  carregando = false;
  respostaProcessada = false;
  rodadaFinalizada = false;

  notificacaoSucesso = false;
  notificacaoErro = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private apiService: ApiService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.codigoUsuario = Number(this.route.snapshot.paramMap.get('codigo'));
    this.carregarExercicios();
  }

  get exercicioAtual() {
    return this.exercicios[this.indiceAtual];
  }

  carregarExercicios() {
    this.carregando = true;
    this.mensagem = '';

    this.apiService.listarExerciciosUsuario(this.codigoUsuario).subscribe({
      next: (resposta: any) => {
        this.usuario = resposta.usuario;
        this.idioma = resposta.idioma;
        this.nivelAtual = resposta.nivel_atual;
        this.pontuacaoTotal = resposta.pontuacao_total;
        this.exercicios = resposta.exercicios;
        this.carregando = false;
        this.cdr.markForCheck();
      },
      error: (erro) => {
        this.carregando = false;
        this.mensagem = erro.status === 400 
          ? 'Você já concluiu este idioma.' 
          : 'Não foi possível carregar os exercícios.';
        this.cdr.markForCheck();
      }
    });
  }

  responder() {
    if (this.respostaProcessada) return;

    if (!this.respostaSelecionada) {
      this.mensagem = 'Selecione uma alternativa.';
      return;
    }

    this.apiService.responderExercicio(this.codigoUsuario, {
      codigo_exercicio: this.exercicioAtual.codigo,
      resposta: this.respostaSelecionada
    }).subscribe({
      next: (resposta: any) => {
        this.pontuacaoTotal = resposta.pontuacao_total;

        if (resposta.acertou) {
          this.exibirNotificacaoSucesso();
        } else {
          this.exibirNotificacaoErro(`Resposta incorreta. Correta: ${resposta.resposta_correta}`);
        }

        this.respostaProcessada = true;
        this.cdr.markForCheck();
      },
      error: () => {
        this.mensagem = 'Não foi possível processar a resposta.';
        this.cdr.markForCheck();
      }
    });
  }

  proximoExercicio() {
    if (this.indiceAtual < this.exercicios.length - 1) {
      this.indiceAtual++;
      this.respostaSelecionada = '';
      this.respostaProcessada = false;
      this.mensagem = '';
      this.esconderNotificacoes();
    }
  }

  finalizarRodada() {
    this.apiService.finalizarRodada(this.codigoUsuario).subscribe({
      next: (resposta: any) => {
        this.nivelAtual = resposta.nivel_atual;
        this.pontuacaoTotal = resposta.pontuacao_total;
        this.rodadaFinalizada = true;

        if (resposta.concluiu) {
          this.mensagem = 'Parabéns! Você concluiu o idioma!';
        } else if (resposta.promoveu) {
          this.mensagem = `Parabéns! Você avançou para o nível ${this.nivelAtual}!`;
        } else {
          const faltam = (this.nivelAtual * 100) - this.pontuacaoTotal;
          this.mensagem = `Você permanece no nível atual. Faltam ${faltam} pontos para avançar.`;
        }

        this.cdr.markForCheck();
      },
      error: () => {
        this.mensagem = 'Não foi possível finalizar a rodada.';
        this.cdr.markForCheck();
      }
    });
  }

  voltar() {
    this.router.navigate(['/home', this.codigoUsuario]);
  }

  private exibirNotificacaoSucesso() {
    this.esconderNotificacoes();
    this.notificacaoSucesso = true;
    setTimeout(() => {
      this.notificacaoSucesso = false;
      this.cdr.markForCheck();
    }, 2000);
  }

  private exibirNotificacaoErro(mensagemErro: string) {
    this.esconderNotificacoes();
    this.mensagem = mensagemErro;
    this.notificacaoErro = true;
    setTimeout(() => {
      this.notificacaoErro = false;
      this.cdr.markForCheck();
    }, 2500);
  }

  private esconderNotificacoes() {
    this.notificacaoSucesso = false;
    this.notificacaoErro = false;
  }
}