import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'TypeScript';

  someNumber = 0;
  someList: number[] = [];
  noScopeNumber = 0;
  usingNGClass = 'myClass';
  myMarginTop = 100;
  name = '';

  constructor(){
    const someConstant = 2;
    this.someNumber = someConstant + 10;

    for (let i = 0; i < 3; ++i){
      this.someList.push(i);
      var x = 5;
    }
    console.log(x);
  }
}
