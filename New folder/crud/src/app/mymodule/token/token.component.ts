import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { FormControl } from '@angular/forms';
import { MyservicesService } from 'src/app/myservices.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-token',
  templateUrl: './token.component.html',
  styleUrls: ['./token.component.css']
})
export class TokenComponent implements OnInit {

  tokenform = new FormGroup({
    token : new FormControl(''),
    username : new FormControl('admin'),
    password : new FormControl('admin')
  })

  constructor(private MyservicesServices:MyservicesService,private router:Router) { }

  ngOnInit(): void {
  }

  onSubmit(){
    this.MyservicesServices.token(this.tokenform.value).subscribe((data:any)=>{
      this.router.navigate(['']).then(() => {
        setTimeout(function() {window.location.reload();} , 2000);
      });
      console.log('token dd',data);
      
    })

  

    

  }

}
