package com.huzaifashahbaz.fragmentsapp;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;
public class MainActivity extends AppCompatActivity {
    boolean isFragmentA=true;
    FragmentManager fragmentManager;
    FragmentTransaction fragmentTransaction;
    FragmentA fragmentA;
    FragmentB fragmentB;
    String messageA="Message from Main for Fragment A";
    String messageB="Message from Main for Fragment B";
    Bundle args=new Bundle();
    public static final String MSG_KEY="MSG_KEY";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        fragmentA=new FragmentA();
        fragmentB=new FragmentB();
        replaceFragment(fragmentA,messageA);
        Button replaceBtn=findViewById(R.id.replace_btn);
        replaceBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!isFragmentA)
                {
                    replaceFragment(fragmentA,messageA);
                    isFragmentA=true;
                }
                else
                {
                    replaceFragment(fragmentB,messageB);
                    isFragmentA=false;
                }
            }
        });
    }
    void replaceFragment(Fragment fragment, String message)
    {
        args.putString(MSG_KEY,message);
        fragment.setArguments(args);
        fragmentManager=getSupportFragmentManager();
        fragmentTransaction=fragmentManager.beginTransaction();
        fragmentTransaction.replace(R.id.frame_container,fragment);
        fragmentTransaction.addToBackStack(null);
        fragmentTransaction.commit();
    }
}