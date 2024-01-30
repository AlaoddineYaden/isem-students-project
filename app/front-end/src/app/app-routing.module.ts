import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PageNotFoundComponent } from './shared/components/page-not-found/page-not-found.component';

const routes: Routes = [
  { path: '', redirectTo: 'home/main', pathMatch: 'full' },
  { path: 'home',
    loadChildren: () => import('./public/public.module').then(x => x.PublicModule)},
   { path: 'etudient',
   loadChildren: () => import('./core/etudient/etudient.module').then(x => x.EtudientModule) } ,
   { path: 'professeur',
   loadChildren: () => import('./core/professeur/professeur.module').then(x => x.ProfesseurModule) } ,
   { path: 'scolarite',
   loadChildren: () => import('./core/scolarite/scolarite.module').then(x => x.ScolariteModule) } ,
 { path: '**', component: PageNotFoundComponent },
  
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
