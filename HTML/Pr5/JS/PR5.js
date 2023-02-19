    /*
    Part 1
    
    console.log("Part 1");
    function numMajor(num1,num2,num3)
    {
        let resposta;
        if(num1>num2 && num1>num3)
        {
            resposta =num1;
            
        }
        if(num2>num1 && num2>num3)
        {
            resposta =num2;
            
        }
        if(num3>num2 && num3>num1)
        {
            resposta =num3;
            
        }
        return "El numero mes alt es: "+resposta;
    }
    console.log(numMajor(12,14,-19));
    console.log(numMajor(21,41,91));

    /*
    Part 2
    
    console.log("Part 2");
    let notesPropies = [3,8.25,10.75,6,0,4,9,7,25]; 
    let notesPropies_2= [8,1.25,12,6,4,6,8,8]; 

    function notaFinal(taulaDeNotes){
        //Suma
        let suma = 0;
        let iteracio=0;
        let resposta;
        for(iteracio=0;iteracio in taulaDeNotes;iteracio++)
        {   
            suma+=taulaDeNotes[iteracio];
        }
        resposta= suma;
        //Divisio 
        
        //resposta = suma/iteracio+1 
        //fiquem +1 ja que la iteracio incia per 0 
        resposta=suma/taulaDeNotes.length; 
        return "la mitjana es de " + resposta;
    }
    console.log(notaFinal(notesPropies));
    console.log(notaFinal(notesPropies_2));
    /*
    Part 3 
    
    console.log("Part 3");
    let Taula=[0,2,5,7];

    function invertir(table)
    {
        let iteracio;
        let resposta=[];
        //Introdueix numero per numero de forma inversa a les iteracions 
        for(iteracio=table.length-1;iteracio >=0;iteracio--)
        {
            resposta.push(table[iteracio]);
        }
        return resposta;
    }
    console.log(Taula);
    console.log(invertir(Taula));
    /*
    Part 4
    */
    console.log("Part 4");

    function comparador(string_1,string_2)
    {
        let resposta;
        if(string_1.length!==string_2.length)//No tienen la misma longitud 
        {
            resposta=false;
        }
        else//Son iguales en cuanto a longitud 
        {
            resposta=true;
        }
        return "Longuitud en comu entre "+string_1+" i "+string_2+": "+resposta;
    }
    console.log(comparador("AA","BB"));
    console.log(comparador("123","1"));
    console.log(comparador("Marc","Anna"));
    /*Extra*/
    //L'usuari introdueix dos string hem de detectar si concideixen els caracters dels strings 
    /*
    function detector(string_1,string_2)
    {
        let num_1 =[];
        let num_2 =[];

        for(let i=0; i <= string_1.length-1;i++)
        {
            num_1.push(string_1[i]);
        }
        for(let i=0; i <= string_2.length-1;i++)
        {
            num_2.push(string_2[i]);
        }

        let lletres_en_comu=[];
        let resposta=false;
        for(let lletra=0;lletra in num_1;lletra++)
        {
            //console.log("Lletra:"+lletra);
            for(let segona=0;segona in num_2;segona++)
            {
                //console.log("Segona:"+segona);
                if(num_1[lletra].toLowerCase()==num_2[segona].toLowerCase())
                {
                    //console.log("Guardat "+num_1[lletra]);
                    lletres_en_comu.push(num_1[lletra]);
                    resposta=true;
                }
            }
        }
        //return "Primero:"+num_1+" Segon:"+num_2;
        return string_1+" i "+string_2+" tenen lletres en comu: "+resposta;

    }
    console.log(detector("HOLA","mon"));
    console.log(detector("oblo","atzar"));
    console.log(detector("cba","abc"));
    */