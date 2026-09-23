import { Routes } from '@angular/router';
import { AcessoComponent } from './pages/acesso/acesso.component';
import { CadastroComponent } from './pages/cadastro/cadastro.component';
import { HomeComponent } from './pages/home/home.component';
import { PraticaComponent } from './pages/pratica/pratica.component';
import { RankingComponent } from './pages/ranking/ranking.component';
import { CertificadoComponent } from './pages/certificado/certificado.component';
import { AdminComponent } from './pages/admin/admin.component';
import { CadastrarIdiomaComponent } from './pages/cadastrar-idioma/cadastrar-idioma.component';
import { CadastrarLicaoComponent } from './pages/cadastrar-licao/cadastrar-licao.component';
import { CadastrarExercicioComponent } from './pages/cadastrar-exercicio/cadastrar-exercicio.component';

export const routes: Routes = [
    {
    path: '',
    component: AcessoComponent
  },
  {
    path: 'cadastro',
    component: CadastroComponent
  },
  {
    path: 'home/:codigo',
    component: HomeComponent
  },
  {
    path: 'pratica/:codigo',
    component: PraticaComponent
  },
  {
    path: 'ranking/:codigo',
    component: RankingComponent
  }, 
  {
    path: 'certificado/:codigo',
    component: CertificadoComponent
  },
  {
    path: 'admin/:codigo',
    component: AdminComponent
  },
  {
    path: 'admin/idioma/:codigo',
    component: CadastrarIdiomaComponent
  },
  {
    path: 'admin/licao/:codigo',
    component: CadastrarLicaoComponent
  },
  {
    path: 'admin/exercicio/:codigo',
    component: CadastrarExercicioComponent
  },
];
