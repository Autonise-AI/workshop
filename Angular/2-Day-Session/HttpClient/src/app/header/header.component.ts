import { Component, OnInit } from '@angular/core';
import { AdminService } from '../admin.service';

@Component({
  selector: 'my-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  links = [
    {link: '/link1', title: 'Link1'}, 
    {link: '/link2', title: 'Link2'}, 
    {link: '/link3', title: 'Link3'}, 
    {link: '/link3', title: 'Link4'}, 
    {link: '/link3', title: 'Link5'}
  ];

  searchValue='Initial Value';

  constructor(public adminService: AdminService) { }

  ngOnInit(): void {
  }

  search(){
    console.log('This is what you searched for: ', this.searchValue);
  }

  switchAdmin(){
    // true, not true = false
    // false, not false = true
    this.adminService.admin = !this.adminService.admin;
  }

}
