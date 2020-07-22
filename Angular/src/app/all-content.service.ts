import { Injectable } from '@angular/core';

export interface ContentInterface{
  header: string;
  headerLink: string;
  img: string;
  imgLink: string;
  lastUpdated: string;
  content: string;
  button: string;
  buttonOnClick: string;
}

@Injectable({
  providedIn: 'root'
})
export class AllContentService {

  public allContents: ContentInterface[] = [
    {
      header: 'NENET: An Edge Learnable Network for Link Prediction in Scene Text',
      headerLink: 'https://arxiv.org/abs/2005.12147',
      img: 'assets/images/HowGCNNWorks.png',
      imgLink: '/research/GraphConvolution',
      lastUpdated: '27th May',
      content: `
          Text detection in scenes based on deep neural networks have shown promising results.
          Instead of using word bounding box regression, recent state-of-the-art methods have started focusing on character bounding box and pixel-level prediction.
          This necessitates the need...
          `,
      button: 'Continue Reading',
      buttonOnClick: 'window.location = "/research/GraphConvolution"',
    },
    {
      header: 'Improving Voice Separation by Incorporating End-to-End Speech Recognition',
      headerLink: 'https://ieeexplore.ieee.org/document/9053845',
      img: 'assets/images/ICASSP2020.png',
      imgLink: '/research/VoiceSeparationn',
      lastUpdated: '26th April',
      content: `
          Recent work in speech separation works good in constrained environments but still perform poorely in noisy backgrounds.
          To further improve voice separation in noisy environments we propose using transfer learning from Automatic Speech Recognition Models.
          We extract…
          `,
      button: 'Continue Reading',
      buttonOnClick: 'window.location = "/research/VoiceSeparation"',
    },
    {
      header: `Research <button type="button" class="btn btn-light btn-outline-dark" onClick="window.open('https://scholar.google.com/citations?hl=en&authuser=1&user=ky_QjGgAAAAJ');">Visit my google scholar profile</button>`,
      headerLink: null,
      img: 'assets/images/research.png',
      imgLink: null,
      lastUpdated: '26th April',
      content: `
      <p>
        My research goal is to understand what intelligence means and trying to reproduce it artificially so that we can have a tool which will reduce the development process drastically in every field. I believe that to achieve this we would require a good understanding of psychology, and an intutive sense of why and how humans function.
      </p>
      <p>
        I started my journey in the academia by focusing on Computer Vision because of its popularity and ease of applicatoin but my interests have diverged into graphs and audio as well.
      </p>
      <p>
        I have mentioned some brief description of my publications below. To get a list of all my publications please visit <a class="" href="/publications">here <i class="fa fa-external-link" style="font-size:12px"></i></a>.
      </p>
      `,
      button: null,
      buttonOnClick: null,
    }
  ];

  home = [0, 1];
  research = [2, 0, 1];
  latest = [0, 1];
  project = [3, 4, 5, 6, 7, 8, 9, 10];

  constructor() {
   }

   getHomeContent(){
    const newContent = [];
    for (const i of this.home){
      newContent.push(this.allContents[i]);
    }
    return newContent;
  }

  getResearchContent(){
    const newContent = [];
    for (const i of this.research){
      newContent.push(this.allContents[i]);
    }
    return newContent;
  }

  getLatestContent(){
    const newContent = [];
    for (const i of this.latest){
      newContent.push(this.allContents[i]);
    }
    return newContent;
  }

  getProjectContent(){
    const newContent = [];
    for (const i of this.project){
      newContent.push(this.allContents[i]);
    }
    return newContent;
  }
}
