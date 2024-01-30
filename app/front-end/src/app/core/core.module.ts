import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EtudientModule } from './etudient/etudient.module';
import { ProfesseurModule } from './professeur/professeur.module';
import { ScolariteModule } from './scolarite/scolarite.module';



@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    EtudientModule,
    ProfesseurModule,
    ScolariteModule
  ]
})
export class CoreModule { }
