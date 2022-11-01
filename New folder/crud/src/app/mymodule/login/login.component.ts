import { Component, OnInit } from '@angular/core';
import { MyservicesService } from 'src/app/myservices.service';
import { FormBuilder } from '@angular/forms';
import { FormControl } from '@angular/forms';
import { FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

@Component({

  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  usernames:any;
  pass:any;
  loginform  = new FormGroup({
    username:new FormControl(''),
    password:new FormControl('')
  })
  constructor(private MyservicesServices:MyservicesService,private router: Router) { }

  ngOnInit(): void {

  }

  onSubmit(){

    
    this.MyservicesServices.user(this.loginform.value).subscribe((data:any)=>{
      console.log('login data',data.access);
      this.router.navigate(['token']).then(() => {
        setTimeout(function() {window.location.reload();} , 2000);
      });
      
    })
  }


}
