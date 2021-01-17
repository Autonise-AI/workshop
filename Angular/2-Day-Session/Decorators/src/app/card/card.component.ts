import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit {

  @Input() title: string;
  @Input() content: string;
  @Input() imageSource: string;

  @Output() myOutput:EventEmitter<string>= new EventEmitter();  

  constructor() { }

  ngOnInit(): void {
  }

  SendValue(){
    this.myOutput.emit(this.title);  
  }


}
