import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  buscarUsuario(codigo: number) {
    return this.http.get(`${this.apiUrl}/usuarios/${codigo}`);
  }

  listarIdiomas() {
    return this.http.get(`${this.apiUrl}/idiomas`);
  }

  cadastrarUsuario(dados: { nome: string; codigo_idioma_aprendizado: number }) {
    return this.http.post(`${this.apiUrl}/usuarios`, dados);
  }

  listarExerciciosUsuario(codigo: number) {
    return this.http.get(`${this.apiUrl}/usuarios/${codigo}/exercicios`);
  }

  responderExercicio(
    codigoUsuario: number,
    dados: {
      codigo_exercicio: number;
      resposta: string;
    },
  ) {
    return this.http.post(`${this.apiUrl}/usuarios/${codigoUsuario}/responder`, dados);
  }

  finalizarRodada(codigoUsuario: number) {
    return this.http.post(`${this.apiUrl}/usuarios/${codigoUsuario}/finalizar-rodada`, {});
  }

  listarRanking() {
    return this.http.get(`${this.apiUrl}/ranking`);
  }

  buscarCertificado(codigo: number) {
    return this.http.get(`${this.apiUrl}/usuarios/${codigo}/certificado`);
  }

  obterCertificadoPdf(codigo: number) {
    return `${this.apiUrl}/usuarios/${codigo}/certificado/pdf`;
  }

  excluirUsuario(codigo: number) {
    return this.http.delete(`${this.apiUrl}/usuarios/${codigo}`);
  }

  cadastrarIdioma(dados: { codigo: number; descricao: string }) {
    return this.http.post(`${this.apiUrl}/idiomas`, dados);
  }

  listarLicoes() {
    return this.http.get(`${this.apiUrl}/licoes`);
  }

  cadastrarLicao(dados: { codigo_idioma: number }) {
    return this.http.post(`${this.apiUrl}/licoes`, dados);
  }

  cadastrarExercicio(dados: {
    codigo_licao: number;
    nivel_dificuldade: number;
    descricao: string;
    opcoes_resposta: string[];
    resposta_correta: string;
    pontuacao: number;
  }) {
    return this.http.post(`${this.apiUrl}/exercicios`, dados);
  }
}
