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
    }
  ];
  constructor() { }
}
