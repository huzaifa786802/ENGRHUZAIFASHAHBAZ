package com.huzaifashahbaz.androidnetworkingusingvolleylibraryapp;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import java.lang.reflect.Method;
public class MainActivity<StringRequest> extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView tv=findViewById(R.id.response_tv);
        RequestQueue queue=volley.newRequestQueue(this);
        String url ="https://www.york.ac.uk/teaching/cws/wws/webpage1.html";
        StringRequest stringRequest=new StringRequest(Request, Method.GET,url,new Response.Listener<String>())
        {
            @Override
            public void onResponse(String response)
            {
                Log.d("Main","Response is"+response);
                tv.setText(response);
            }
        };
        new Response.ErrorListener()
        {
            @Override
            public void onErrorResponse(VolleyError error)
            {
                Log.d("Main","No response");
            }
        };
    }
}