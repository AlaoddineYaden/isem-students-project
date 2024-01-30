import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  // { path: 'home', redirectTo: 'home/main', pathMatch: 'full' },

  // {
  //   path: 'home',
  //   component: ContainerComponent,
  //   children: [
  //     { path: 'main', component: MainComponent },
  //     { path: 'login', component: LoginComponent },
  //     { path: 'signup', component: SignupComponent },
  //     { path: 'forgot-password', component: ForgotPasswordComponent },
  //     { path: 'verify-email-address', component: VerifyEmailComponent },
  //   ],
  // },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PublicRoutingModule {}
