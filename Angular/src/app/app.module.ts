import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ContentComponent } from './reuse/content/content.component';
import { ProfileComponent } from './profile/profile.component';
import { HomeComponent } from './home/home.component';
import { ResearchComponent } from './research/research.component';
import { LatestComponent } from './latest/latest.component';
import { ProjectComponent } from './project/project.component';
import { SafeHtmlPipe } from './safe-html.pipe';
import { ContactComponent } from './contact/contact.component';
@NgModule({
  declarations: [
    AppComponent,
    ContentComponent,
    ProfileComponent,
    HomeComponent,
    ResearchComponent,
    LatestComponent,
    ProjectComponent,
    SafeHtmlPipe,
    ContactComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
