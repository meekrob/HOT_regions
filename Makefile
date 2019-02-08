L=~/local/support_data/ce10/ce10ToCe11.over.chain.gz
C=ce11.chrom.sizes

ce11.regions_w_color_score.bed: ce11.regions_w_score.bed
	python3 make_big_bedable.py $^ > $@

ce11.regions_w_score.bed:
	paste HOTregions.ce11.bed HOTregions_ce10.txt hot_scores.ecdf > $@

%.ce10.bed: %_ce10.txt
	./regionsToBed.py $^ | sort -k1,1 -k2,2n  > $@
	
%.ce11.bed: %.ce10.bed
	liftOver $^ $L $@ $*.ce10.unmapped 

top_01.ix: top_01.terms
	ixixx top_01.terms top_01.ix  top_01.ixx

#%.bb: %.bed
	#bedToBigBed $^ $C $@ -type=bed9 -extraIndex=name -as=hot_regions.as
	#bigBedInfo $@

# don't care about the extra indexes anymore
%.bb: %.bed
	bedSort $^ $^
	bedToBigBed $^ $C $@ -type=bed9 -as=hot_regions.as
	bigBedInfo $@
