import { Component, OnInit } from '@angular/core';
import {AllContentService} from '../all-content.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  homeContent = null;

  constructor(public allContents: AllContentService) {
    this.homeContent = allContents.getHomeContent();
  }
  ngOnInit(): void {
  }

}
