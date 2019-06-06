# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GenedbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()  # INTEGER      autoIncrement,primaryKey
    symbol = scrapy.Field()  # STRING(255)
    name = scrapy.Field()  # TEXT
    abstract = scrapy.Field()  # TEXT
    description = scrapy.Field()  # TEXT
    location = scrapy.Field()  # STRING(10)
    region_start = scrapy.Field()  # INTEGER
    region_end = scrapy.Field()  # INTEGER
    band = scrapy.Field()  # STRING(50)


class EntrezItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    entrez_id = scrapy.Field()  # INTEGER      autoIncrement,primaryKey


class GeneNameItem(scrapy.Item):
    ena = scrapy.Field()
    symbol = scrapy.Field()
    entrez_id = scrapy.Field()
    name = scrapy.Field()
    ensembl_gene_id = scrapy.Field()
    ccds_id = scrapy.Field()
    prev_name = scrapy.Field()
    ucsc_id = scrapy.Field()
    uniprot_ids = scrapy.Field()
    vega_id = scrapy.Field()
    refseq_accession = scrapy.Field()
    status = scrapy.Field()
    prev_symbol = scrapy.Field()
    mgd_id = scrapy.Field()
    locus_type = scrapy.Field()
    alias_symbol = scrapy.Field()
    alias_name = scrapy.Field()
    hgnc_id = scrapy.Field()
    locus_group = scrapy.Field()
    rgd_id = scrapy.Field()
    lsdb = scrapy.Field()
    lncipedia = scrapy.Field()
    iuphar = scrapy.Field()
    gene_group_id = scrapy.Field()
    gene_group = scrapy.Field()
    mamit_trnadb = scrapy.Field()
    lncrnadb = scrapy.Field()
    location = scrapy.Field()
    cd = scrapy.Field()
    date_name_changed = scrapy.Field()
    snornabase = scrapy.Field()
    rna_central_id = scrapy.Field()
    mirbase = scrapy.Field()
    horde_id = scrapy.Field()
    date_symbol_changed = scrapy.Field()
    kznf_gene_catalog = scrapy.Field()
    orphanet = scrapy.Field()
    enzyme_id = scrapy.Field()
    cosmic = scrapy.Field()
    imgt = scrapy.Field()
    gtrnadb = scrapy.Field()
    uuid = scrapy.Field()
    location_sortable = scrapy.Field()
    omim_id = scrapy.Field()
    pubmed_id = scrapy.Field()
    merops = scrapy.Field()
    date_approved_reserved = scrapy.Field()
    pseudogene_org = scrapy.Field()
    date_modified = scrapy.Field()
    version = scrapy.Field()
    bioparadigms_slc = scrapy.Field()
    homeodb = scrapy.Field()
    intermediate_filament_db = scrapy.Field()
