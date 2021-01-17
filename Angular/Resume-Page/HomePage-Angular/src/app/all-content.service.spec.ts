import { TestBed } from '@angular/core/testing';

import { AllContentService } from './all-content.service';

describe('AllContentService', () => {
  let service: AllContentService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AllContentService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
