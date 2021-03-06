import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  header = '';

  // cardContent = [{
  //   content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
  //   title: 'First Card',
  //   imageSource: 'https://mayank.autonise.com/static/Images/Content/IDRiD/IDRiD.png'
  // },{
  //   content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
  //   title: 'My Resume Point 2',
  //   imageSource: 'https://mayank.autonise.com/static/Images/Content/VoiceSeparation/ICASSP2020.png'
  // },{
  //   content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
  //   title: 'My Resume Point 3',
  //   imageSource: 'https://mayank.autonise.com/static/Images/Content/TextDetectionCRAFT/craft_example.gif'
  // }]

  cardContent = [
    {
      content: 'Content 1',
      title: 'Title 1',
      imageSource: 'Image Source 1'
    }, 
    {
      content: 'Content 2',
      title: 'Title 2',
      imageSource: 'Image Source 1'
    }, 
    {
      content: 'Content 2',
      title: 'Title 2',
      imageSource: 'Image Source 1'
    }
  ];

  ProcessChildData(data){
    this.header = data;
  }
}
