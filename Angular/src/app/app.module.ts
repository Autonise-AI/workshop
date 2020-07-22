import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ContentComponent } from './reuse/content/content.component';
import { ProfileComponent } from './profile/profile.component';
import { HomeComponent } from './home/home.component';
import { ResearchComponent } from './research/research.component';
import { LatestComponent } from './latest/latest.component';
import { ProjectComponent } from './project/project.component';
import { PublicationComponent } from './publication/publication.component';
import { SafeHtmlPipe } from './safe-html.pipe';

@NgModule({
  declarations: [
    AppComponent,
    ContentComponent,
    ProfileComponent,
    HomeComponent,
    ResearchComponent,
    LatestComponent,
    ProjectComponent,
    PublicationComponent,
    SafeHtmlPipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
