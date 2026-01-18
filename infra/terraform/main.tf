provider "google" {
  project =  "projectolist-483623"
  credentials = file("/Users/gustavo/Documents/Projetos/project-olist/projectolist-483623-63de0f11da4d.json")
}

resource "google_storage_bucket" "bucket_olist" {
  name = "bucket_olist"
  location = "US"
  storage_class = "STANDARD"
  uniform_bucket_level_access = true
}

resource "google_bigquery_dataset" "dataset_olist" {
  dataset_id                  = "olist_silver"
  friendly_name               = "Olist Dataset Silver"
  description                 = "Dataset Silver"
  location                    = "US" 
  default_table_expiration_ms = 3600000

  labels = {
    env = "default"
  }
}