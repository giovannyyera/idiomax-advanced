import {
  ChangeDetectorRef,
  Component
} from '@angular/core';

import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';

import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-ranking',
  standalone: true,
  imports: [
    CommonModule
  ],
  templateUrl: './ranking.component.html',
  styleUrl: './ranking.component.css'
})
export class RankingComponent {
  ranking: any[] = [];
  mensagem = '';
  carregando = false;

  codigoUsuario = 0;

  constructor(
    private apiService: ApiService,
    private router: Router,
    private route: ActivatedRoute,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.codigoUsuario = Number(
        this.route.snapshot.paramMap.get('codigo')
    );

    this.carregarRanking();
  }

  carregarRanking() {
    this.carregando = true;

    this.apiService.listarRanking()
      .subscribe({
        next: (ranking: any) => {
          this.ranking = ranking;
          this.carregando = false;

          this.cdr.markForCheck();
        },

        error: () => {
          this.carregando = false;
          this.mensagem =
            'Não foi possível carregar o ranking.';

          this.cdr.markForCheck();
        }
      });
  }

  voltar() {
    this.router.navigate([
        '/home',
        this.codigoUsuario
    ]);
    }

  sair() {
    this.router.navigate([
      '/'
    ]);
  }
}