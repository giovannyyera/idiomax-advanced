import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.css',
})
export class AdminComponent {
  codigoUsuario = 0;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
  ) {}

  ngOnInit() {
    this.codigoUsuario = Number(this.route.snapshot.paramMap.get('codigo'));
  }

  irParaIdioma() {
    this.router.navigate(['/admin/idioma', this.codigoUsuario]);
  }

  irParaLicao() {
    this.router.navigate(['/admin/licao', this.codigoUsuario]);
  }

  irParaExercicio() {
    this.router.navigate(['/admin/exercicio', this.codigoUsuario]);
  }

  voltar() {
    this.router.navigate(['/home', this.codigoUsuario]);
  }
}
