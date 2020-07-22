import { Component, OnInit } from '@angular/core';
import {AllContentService} from '../all-content.service';

@Component({
  selector: 'app-latest',
  templateUrl: './latest.component.html',
  styleUrls: ['./latest.component.css']
})
export class LatestComponent implements OnInit {

  latestContent = null;

  constructor(public allContents: AllContentService) {
    this.latestContent = allContents.getLatestContent();
  }
  ngOnInit(): void {
  }

}
