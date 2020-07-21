import { Component, OnInit } from '@angular/core';
import {AllContentService} from '../all-content.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(public allContents: AllContentService) { }

  ngOnInit(): void {
  }

}
