import { Component } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Mayank Kumar Singh';
  active = null;
  constructor(router: Router) {
    router.events.forEach((event) => {
      if (event.url !== undefined){
        this.active = event.url;
      }
      // if (event instanceof NavigationStart) {
      // }
      // NavigationEnd
      // NavigationCancel
      // NavigationError
      // RoutesRecognized
    });
  }
}
