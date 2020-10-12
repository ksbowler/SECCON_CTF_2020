from Crypto.Util.number import *


N = 13234306273608973531555502334446720401597326792644624514228362685813698571322410829494757436628326246629203126562441757712029708148508660279739210512110734001019285095467352938553972438629039005820507697493315650840705745518918873979766056584458077636454673830866061550714002346318865318536544606580475852690351622415519854730947773248376978689711597597169469401661488756669849772658771813742926651925442468141895198767553183304485662688033274567173210826233405235701905642383704395846192587563843422713499468379304400363773291993404144432403315463931374682824546730098380872658106314368520370995385913965019067624762624652495458399359096083188938802975032297056646831904294336374652136926975731836556951432035301855715375295216481079863945383657
c = 9094564357254217771457579638296343398667095069849711922513911147179424647045593821415928967849073271368133854458732106409023539482401316282328817488781771665657515880026432487444729168909088425021111879152492812216384426360971681055941907554538267523250780508925995498013624610554177330113234686073838491261974164065812534037687990653834520243512128393881497418722817552604416319729143988970277812550536939775865310487081108925130229024749287074763499871216498398695877450736179371920963283041212502898938555288461797406895266037211533065670904218278235604002573401193114111627382958428536968266964975362791704067660270952933411608299947663325963289383426020609754934510085150774508301734516652467839087341415815719569669955613063226205647580528


hN = hex(N)

def calc(p,q,times):
	times += 1
	for i in range(10):
		temp_p = "3" + str(i) + p
		int_p = int(temp_p,16)
		if N%int_p == 0:
			print(int_p,N//int_p)
			return (int_p,N//int_p)
		for j in range(10):
			temp_q = "3" + str(j) + q
			int_q = int(temp_q,16)
			if N%int_q == 0:
				print(int_q,N//int_q)
				return (int_q,N//int_q)
			pq = int_p*int_q
			str_pq = hex(pq)
			if str_pq[-times*2:] == hN[-times*2:]:
				ans_p,ans_q = calc(temp_p,temp_q,times)
				if ans_p and ans_q:
					return ans_p,ans_q

	return 0,0


p,q = calc("","",0)
#p = 3637611432709594371264704511468609728682607388876384102923818225109063398544210545492359167474530302718857062208163788154545487196383201100099744936786539425111292220021228975618912348451653498292968706501356033542981209543303382618915960925499336225494396632251587816534249173299308575077124763020932984069489928758050796814780366273657518663455127893432325623882626511921
#q = 3638185803630753864335217383395842181508119024909369128797457096191118728152545787687455274852407358549179060470936614685236622618451962852275333560535721913986108552149843022144549040204005933770920575972750848156366347104162613708380917302979323126150715081205828598321923327391861468388848094921651840175816922414046570530147719708444089371292632394192960886439467561017

phi = (p-1)*(q-1)

e = 65537

d = inverse(e,phi)

mes = pow(c,d,N)
print(long_to_bytes(mes))
