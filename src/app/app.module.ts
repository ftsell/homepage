import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AngularFontAwesomeModule} from "angular-font-awesome";

import {AppComponent} from './app.component';
import {TaskbarComponent} from './taskbar/taskbar.component';
import {AngularDraggableModule} from "angular2-draggable";
import {HttpClientModule} from "@angular/common/http";
import {WidgetComponent} from './widget/widget.component';
import {WindowsUpdateComponent} from "./widget/windows-update.component";
import {ServiceWorkerModule} from '@angular/service-worker';
import {environment} from "../environments/environment";
import {PixelflutComponent} from './widget/pixelflut/pixelflut.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskbarComponent,
    WidgetComponent,
    WindowsUpdateComponent,
    PixelflutComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule,
    AngularDraggableModule,
    HttpClientModule,
    ServiceWorkerModule.register('ngsw-worker.js', {enabled: environment.production})
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
