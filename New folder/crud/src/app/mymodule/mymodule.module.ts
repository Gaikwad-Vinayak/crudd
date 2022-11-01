import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MycomponentComponent } from './mycomponent/mycomponent.component';
import { MatSliderModule } from '@angular/material/slider';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatIconModule} from '@angular/material/icon';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import { TokenComponent } from './token/token.component';
@NgModule({
  declarations: [
    MycomponentComponent,
    LoginComponent,
    TokenComponent
  ],
  imports: [
    CommonModule,
    MatSliderModule,
    MatButtonModule,
    MatToolbarModule,
    MatIconModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  exports:[
    MycomponentComponent,
    LoginComponent,
    TokenComponent,
  ]
})
export class MymoduleModule { }
