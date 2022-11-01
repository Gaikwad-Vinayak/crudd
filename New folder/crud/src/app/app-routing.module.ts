import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './mymodule/login/login.component';
import { MycomponentComponent } from './mymodule/mycomponent/mycomponent.component';
import { TokenComponent } from './mymodule/token/token.component';
const routes: Routes = [
  { path: '', component: MycomponentComponent },
  { path: 'login', component: LoginComponent},
  { path: 'token', component: TokenComponent },
  { path: '**', redirectTo: 'login' }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
