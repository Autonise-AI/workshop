import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'yes';

  cardContent = [];

  constructor(private http: HttpClient){
    http.get('https://www.autonise.com/api/users/getCatalog').subscribe((res: any) => {
      console.log(res);
      for (let catalogI of res.catalog){
        this.cardContent.push({
          content: catalogI.description,
          title: catalogI.title,
          imageSource: 'https://www.autonise.com' + catalogI.icon,
        });
      }
    });
  }
}
