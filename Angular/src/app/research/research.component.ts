import { Component, OnInit } from '@angular/core';
import {AllContentService} from '../all-content.service';

@Component({
  selector: 'app-research',
  templateUrl: './research.component.html',
  styleUrls: ['./research.component.css']
})
export class ResearchComponent implements OnInit {

  researchContent = null;

  constructor(public allContents: AllContentService) {
    this.researchContent = allContents.getResearchContent();
  }
  ngOnInit(): void {
  }

}
