import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrls: ['./content.component.css']
})
export class ContentComponent implements OnInit {
  @Input() header = 'Not Found';
  @Input() headerLink = 'Not Found';
  @Input() img = 'Not Found';
  @Input() imgLink = 'Not Found';
  @Input() lastUpdated = 'Not Found';
  @Input() content = 'Not Found';
  @Input() button = 'Not Found';
  @Input() buttonOnClick = 'Not Found';
  constructor() { }

  ngOnInit(): void {
  }

  evaluate(){
    eval(this.buttonOnClick);
  }

}
