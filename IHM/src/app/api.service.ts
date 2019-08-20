import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';

Injectable({
  providedIn: 'root'
})


const endpoint = 'http://127.0.0.1:5000/api/v1.0/arrosage/';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

export class ApiService {

  constructor(private http: HttpClient) { }

  private extractData(res: Response) {
    let body = res;
    return body || { };
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
  
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
  
      // TODO: better job of transforming error for user consumption
      console.log(`${operation} failed: ${error.message}`);
  
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  postHerbe(time : Number): Observable<any> {
    console.log('posting herbe');
    return this.http.post(endpoint + 'herbe', {"action": "on","temps": time}).pipe(
      catchError(this.handleError<any>('addProduct'))
    );
  }

  postPotager(): Observable<any> {
    return this.http.get(endpoint + 'products').pipe(
      map(this.extractData));
  }

}

