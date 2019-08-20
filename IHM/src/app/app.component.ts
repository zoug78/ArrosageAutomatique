import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'IHM';

  constructor(public api:ApiService) {}

  handleHerbe() {
    console.log("here")
    this.api.postHerbe(30).subscribe(res => {
      console.log('rez=' + res)
    }, (err) => {
      console.log(err);
    }
  );
  }
}
