import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {
  public emailID: string;
  public content: string;
  public errorMessageEmpty = false;
  public errorEmailEmpty = false;
  constructor() { }

  ngOnInit(): void {
  }

  submitForm(){
    if (!this.content){
      this.errorMessageEmpty = true;
    }
    else{
      this.errorMessageEmpty = false;
    }
    if (!this.emailID){
      this.errorEmailEmpty = true;
    }
    else{
      this.errorEmailEmpty = false;
    }
    if (this.emailID && this.content){
      this.errorMessageEmpty = false;
      this.errorEmailEmpty = false;
      console.log(this.emailID);
      console.log(this.content);
    }
  }

  keyDownFunction(event) {
    if (event.keyCode === 13) {
      this.submitForm();
    }
  }

}
