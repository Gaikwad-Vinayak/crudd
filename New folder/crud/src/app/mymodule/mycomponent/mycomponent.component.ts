import { Component, OnInit } from '@angular/core';
import * as $ from "jquery";
import { MyservicesService } from 'src/app/myservices.service';
import { FormGroup } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { FormControl } from '@angular/forms';
import { ResourceLoader } from '@angular/compiler';
// import Swal from 'sweetalert2/dist/sweetalert2.js';
import Swal from 'sweetalert2'
import { data } from 'jquery';

@Component({
  selector: 'app-mycomponent',
  templateUrl: './mycomponent.component.html',
  styleUrls: ['./mycomponent.component.css']
})
export class MycomponentComponent implements OnInit {

  apidata:any=[] 

  MyComponentForm  = new FormGroup({
    name:new FormControl(''),
    email:new FormControl(''),
    roll:new FormControl(''),
  })
  
  constructor(private MyservicesServices:MyservicesService) { }

  ngOnInit(): void {



    // this.listofform();
    this.listofdata();
    

    this.MyservicesServices.getdata().subscribe((data:any)=>{
      this.apidata = data
      console.log(data,'data');
      
    })
  }
  

  
  
  

  onSubmit(){
    console.log(this.MyComponentForm);
      Swal.fire(
        'Submited!',
        'Your Data Submit',
        'success'
      ).then((result)=>{
        if(result.isConfirmed){
          setTimeout(
            function(){
              window.location.reload()
            })}})
            
    this.MyservicesServices.savedata(this.MyComponentForm.value).subscribe((data:any)=>{
      console.log(data,'save data');
    })
  }


  onDeletedata(id:any){
    Swal.fire({
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Deleted!',
          'Your file has been deleted.',
          'success'
        ).then((result)=>{
          if(result.isConfirmed){
            setTimeout(
              function(){
                window.location.reload()

              })}})

        // .then((result) => {
        //   if (result.isDenied) {
        //   setTimeout(
        //     function(){ 
        //     location.reload(); 
        //     }, 10000);
        // ))}
        // window.location.reload(); 
        
      }
    })
    this.MyservicesServices.deletedata(id).subscribe((data:any)=>{
      console.log(id,'delete data');
      
    })

  }

  onEidit(apidata:any){
      this.MyComponentForm.patchValue({
        // ID: apidata.id,
        name: apidata.name,
        email: apidata.email,
        roll: apidata.roll
      });
      
          
    var id=$("#ID").val();
    console.log(id,'id');
    
		if(id!='')
		{
      $("#list_form").show();
      $("#list_table").hide();
      $("#listofform").hide();
      $("#listofdata").show();
      $("#submitbtn").hide();
      $("#update").show();
		}

  }
  listofform(){
    $("#list_form").show();
    $("#list_table").hide();
    $("#listofform").hide();
    $("#listofdata").show();
    $("#update").hide();
    $("#submitbtn").show();
    
  }
  listofdata(){
    $("#list_form").hide();
    $("#list_table").show();
    $("#listofform").show();
    $("#listofdata").hide();
 

  }

  


  

}
