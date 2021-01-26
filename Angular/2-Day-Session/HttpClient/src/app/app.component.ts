import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'yes';

  cardContent = [
    // {content: '', title: '', imageSource: ''}
  ];

  constructor(private http: HttpClient){

    http.get('https://www.autonise.com/api/users/getCatalog').subscribe((res: any) => {
      console.log(res);

      for (let catalogI of res.catalog){
        // append, 
        console.log(catalogI.description)
        console.log(catalogI.title, catalogI.icon, 'catalog');
        this.cardContent.push({
          content: catalogI.description,
          title: catalogI.title,
          imageSource: 'https://digger-project.com/wp-content/uploads/2020/05/ICASSP-2020.png',
        });
      }
    });

    // Code for posting data to the server. 
    // Warning! This code will not work as the server has not been configured for post method

    // http.post(
    //   'https://www.autonise.com/api/users/getCatalog', 
    //   {data: "I am trying to communicate with the server"}
    // ).subscribe((res: any) => {
    //   console.log(res);

    //   for (let catalogI of res.catalog){
    //     // append, 
    //     console.log(catalogI.description)
    //     console.log(catalogI.title, catalogI.icon, 'catalog');
    //     this.cardContent.push({
    //       content: catalogI.description,
    //       title: catalogI.title,
    //       imageSource: 'https://digger-project.com/wp-content/uploads/2020/05/ICASSP-2020.png',
    //     });
    //   }
    // });

  }
}
