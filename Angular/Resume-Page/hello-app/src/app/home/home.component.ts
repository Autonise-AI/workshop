import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  contentHeading = ['Header1', 'Header2'];

  constructor() { }

  ngOnInit(): void {
    let emptyParent = document.getElementById('empty');

    let newDiv = document.createElement('div');
    newDiv.classList.add('container');
    newDiv.classList.add('bg-light');
    newDiv.classList.add('my-3');

    let newRow = document.createElement('div');
    newRow.classList.add('row');

    let newCol = document.createElement('div');
    newCol.classList.add('col');

    newCol.innerHTML = this.contentHeading[0];

    newRow.appendChild(newCol);
    newDiv.appendChild(newRow);

    emptyParent.appendChild(newDiv);

  }

}
