import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

const baseUrl = 'http://127.0.0.1:8000/user/'

const veryfytoken = 'http://127.0.0.1:8000/veryfy/'
const usertoken = 'http://127.0.0.1:8000/gettoken/'

@Injectable({
  providedIn: 'root'
})

export class MyservicesService {

  constructor(private Http:HttpClient) { }

  token(data:any){
    return this.Http.post(veryfytoken,data)

  }

  user(data:any){
    return this.Http.post(usertoken,data)
  }
  getdata(){
    return this.Http.get(baseUrl)
  }

  savedata(data:any){
    return this.Http.post(baseUrl,data)
  }
  deletedata(id:any){
    return this.Http.delete(`${baseUrl}${id}`)
  }
  updatedata(id:any){
    return this.Http.put(baseUrl,id)
  }
}
