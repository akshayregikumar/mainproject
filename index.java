 package com.example.user.digitalspace;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import java.util.logging.Handler;
 //////////VISHNU P.R.     vishnu.prvishnu@outlook.com
 public class index extends AppCompatActivity {
private static int TO=3000;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_index);
        //new Handler().postDelayed(new Runnable(){
        new android.os.Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
               // Intent home=new Intent(index.this,login3.class);
                Intent home=new Intent(index.this,login3.class);
                startActivity(home);
                finish();
            }
        },TO);
          /*  @Override
                    public void run()
            {
                Intent home=new Intent(index.this,home.class);
                startActivity(home);
                finisd();
            }
        },TO);*/
    }
}
