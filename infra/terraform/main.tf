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

