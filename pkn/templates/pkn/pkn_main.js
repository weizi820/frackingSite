//PKN
//   ----------------------------------------------------------------------
//   Created by Endrina Rivas
//       endrina.rivas@uwaterloo.ca
//       Department of Civil Engineering
//       University of Waterloo
//   Last Updated June 2017
//   INCOMPLETE!
//   References: 
//       [1] Nordgren, R. P. (1972). Propagation of a Vertical Hydraulic 
//           Fracture. Society of Petroleum Engineers Journal, 12(4), 306–314. 
//       [2] Valko, P., & Economides, M. J. (1995). Hydraulic Fracture Mechanics. 
//           New York: John Wiley & Sons.
//       [3] Yew, C. H. (1997). Mechanics of hydraulic fracturing. 
//           Houston, Tex: Gulf Pub. Co.
//   ----------------------------------------------------------------------

	function newDesign() {
		document.querySelector(".main-screen").style.display = 'none';
		document.querySelector(".results-screen").style.display = 'none';
		document.querySelector(".design-input-screen").style.display = 'block';
	};

	function newAnalysis() {
		document.querySelector(".main-screen").style.display = 'none';
		document.querySelector(".results-screen").style.display = 'none';
		document.querySelector(".analysis-input-screen").style.display = 'block';
	};

	function homePage() {
		document.querySelector(".design-input-screen").style.display = 'none';
		document.querySelector(".analysis-input-screen").style.display = 'none';
		document.querySelector(".results-screen").style.display = 'none';
		document.querySelector(".help-screen").style.display = 'none';
		document.querySelector(".error-screen").style.display = 'none';
		document.querySelector(".main-screen").style.display = 'block';
	};

	function help() {
		document.querySelector(".main-screen").style.display = 'none';
		document.querySelector(".help-screen").style.display = 'block';
	};

	function designPKN() {
		try{
			document.querySelector(".design-input-screen").style.display = 'none';
			document.querySelector(".results-screen").style.display = 'block';

			// Input main variables
				var input = document.getElementById("designForm");

				var L = input.elements[0].value;

				var E = input.elements[1].value;
				var nu = input.elements[2].value;

				var H = input.elements[3].value;

				var mu = input.elements[4].value;
				var Q = input.elements[5].value;
				var C = input.elements[6].value;
				var S = input.elements[7].value;
				var materialBalance = input.elements[8].value;

			// Calculate material parameterss
				// plain strain modulus
				var E_plane = E/(1-nu^2);
				// shear modulus
				var G = E/2/(1+nu);

			// Design the length of the stimulation

				// TODO: figure out how to find zeros a function in js. 
				// look into math.js
				switch (materialBalance) {
					case "No Leak": 
			            // Ref. [2] Eqn. 9.13
			            var t = (L/0.524/(Q^3 * E_plane/mu/H^4)^(1/5))^(5/4);
			            // Ref. [3] Eqn. 1-21
			            var t2 = (L/0.68/(G*Q^3/(1-nu)/mu/H^4)^(1/5))^(5/4);
					case "Carter":
			            // Ref. [2] Eqn. 9.41
			            var w_avg = 2.05*(mu*q*L/E_plane)^(1/4);
			            // Ref. [2] Eqn. 9.42
			            var beta = 2*C*sqrt(pi*t)/(w_avg(L)+2*Sp);
		                // Ref. [2] Eqn. 9.42
		                fun = L - (w_avg(L) + 2*Sp)*q / 4/C^2/pi/h*
		                    (exp(beta(L,t)^2)*erfc(beta(L,t)) + 2*beta(L,t)/sqrt(pi) - 1);
		                t = fzero(fun,1);
					case "Large Leak":
		                // Ref. [2] Eqn. 1-18
		                // var t = L*Math.PI*C*H;                                                                                                                                                                                                                                                                                                                                                                           /Q)^2;
				};

			// Calculate fracture width and net pressure
		        // fracture width at the wellbore Ref. [2] Eqn. 9.40
		        var ww0 = 3.27*(Q*mu*L/E_plane)^(1/4);
		        // net pressure at the wellbore Ref. [2] Eqn. 9.1
		        var pnw = E_plane/2/H*ww0;
		        
		        // fracture width at the wellbore Ref. [3] Eqn. 1-22
		        var ww02 = 2.5*((1-nu)*mu*Q^2/G/H)^(1/5)*t^(1/5);
		        // net pressure at the wellbore Ref. [3] Eqn. 1-23
		        var pnw2 = 2.5*(G^4*mu*Q^2/(1-nu)^4/H^6)^(1/5)*t^(1/5);
		        
		        // NOTE: these two equations give slightly different results
				
			// Display results
				document.getElementById("result").innerHTML = "The time required to propagate crack " 
								+ L + " [length] is " + t + " [time]." + 
								"The net pressure at this time is " + pnw2 + " [pressure], and "
								+ "the fracture width at the wellbore is " + ww02 + " [length].";
		}
		catch(err) {
			document.querySelector(".design-input-screen").style.display = 'none';
			document.querySelector(".results-screen").style.display = 'none';
			document.querySelector(".error-screen").style.display = 'block';
		};
	};

	function analysePKN() {
		document.querySelector(".analysis-input-screen").style.display = 'none';
		document.querySelector(".results-screen").style.display = 'block';

		// Input main variables
			var input = document.getElementById("analysisForm");

			var tStart = input.elements[0].value;
			var tEnd = input.elements[1].value;
			var dt = input.elements[2].value;

			var E = input.elements[3].value;
			var nu = input.elements[4].value;

			var H = input.elements[5].value;

			var mu = input.elements[6].value;
			var Q = input.elements[7].value;
			var C = input.elements[8].value;
			var S = input.elements[9].value;
			var materialBalance = input.elements[10].value;

		// Calculate material parameterss
			// plain strain modulus
			var E_plane = E/(1-nu^2);
			// shear modulus
			var G = E/2/(1+nu);

			// Compute the length of the stimulated crack
			// switch (materialBalance) {
			// 	case "No Leak": 
		 //            // Ref. [2] Eqn. 9.13
		 //             // L = 0.524*(q^3*E_plane/mu/h^4)^(1/5)*t.^(4/5); 
		 //            var L = (625/512/pi^3)^(1/5)*(q^3*E_plane/mu/h^4)^(1/5)*t.^(4/5); 
		 //            // Ref. [3] Eqn. 1-21
		 //            var L2 = 0.68*(G*q^3/(1-nu)/mu/h^4)^(1/5)*t^(4/5);
			// 	case "Carter":
		 //            // Ref. [2] Eqn. 9.41
		 //            var w_avg = @(L) 2.05*(mu*q*L/E_plane)^(1/4);
		 //            // Ref. [2] Eqn. 9.42
		 //            var beta = @(L,t) 2*C*sqrt(pi*t)/(w_avg(L)+2*Sp);
	  //               // Ref. [2] Eqn. 9.42
	  //               fun = @(L) L - (w_avg(L) + 2*Sp)*q / 4/C^2/pi/h*...
	  //                   (exp(beta(L,t)^2)*erfc(beta(L,t)) + 2*beta(L,t)/sqrt(pi) - 1);
	  //               L = fzero(fun,1);
			// 	case "Large Leak":
	  //               // Ref. [3] Eqn. 1-18
	  //               L = q/pi/C/h*t^(1/2);
			// }

		// Calculate fracture width and net pressure
	        // fracture width at the wellbore Ref. [2] Eqn. 9.40
	        // var ww0 = 3.27*(q*mu*L/E_plane).^(1/4);
	        // // net pressure at the wellbore Ref. [2] Eqn. 9.1
	        // var pnw = E_plane/2/h.*ww0;
	        
	        // // fracture width at the wellbore Ref. [3] Eqn. 1-22
	        // var ww02 = 2.5*((1-nu)*mu*q^2/G/h).^(1/5)*t^(1/5);
	        // // net pressure at the wellbore Ref. [3] Eqn. 1-23
	        // var pnw2 = 2.5*(G^4*mu*q^2/(1-nu)^4/h^6)^(1/5)*t^(1/5);
	        
	        // NOTE: these two equations give slightly different results
			
	    // Display results
			// document.getElementById("result").innerHTML = "The time required to propagate crack " 
			// 				+ L + " [length] is " + t + " [time]." + 
			// 				"The net pressure at this time is " + pnw2 + " [pressure], and "
			// 				+ "the fracture width at the wellbore is " + ww02 + " [length].";


		};


	// 	// TODO: figure out how to display figures 
	// 	// Options:  Google charts, chart.js, plotly, chartist.js, uvCharts, D3.js, Flot, 
	// 	// https://www.sitepoint.com/15-best-javascript-charting-libraries/

	// 	// http://www.jscharts.com/how-to-use-line-graphs
	// 	var myChart = new JSChart('chartid','line');
	// 	myChart.setDataArray(myData);
	// 	myChart.setAxisNameX('Time');
	// 	myChart.setAxisNameY('Length');
	// 	myChart.setAxisTitle('Crack length over time')
	// 	myChart.draw();

	// 	// window.alert("success");
	// };


//     if length(t) > 1
//         figure(1)
//         // plot length over time
//         subplot(4,1,1)
//         plot(t,L)
//         hold on 
//         plot(t,L2)
//         xlabel('time')
//         ylabel('length')
        
//         // plot maximum width over time
//         subplot(4,1,2)
//         plot(t,ww0)
//         hold on 
//         plot(t,ww02)
//         xlabel('time')
//         ylabel('max. width')

//         // plot net pressure over time
//         subplot(4,1,3)
//         plot(t,pnw)
//         hold on 
//         plot(t,pnw2)
//         xlabel('time')
//         ylabel('net pressure')

//         // plot width over length
//         subplot(4,1,4)
//         plot(ww0,L)
//         hold on 
//         plot(ww0,L2)
//         xlabel('max. width')
//         ylabel('length')
//         legend('Valko','Yew')
//     end
    
//     // plot the crack geometry over time
//     figure(2)
//     for i = 1:length(t)
//         [x,y,z] = ellipsoid(0,0,0,L(i)/2,ww0(i)/2,L(i)/2,30);
//         surf(x,y,z)
//     end

//  Python calculations may be more flexible than javascript