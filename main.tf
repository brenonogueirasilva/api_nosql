resource "google_compute_instance" "default" {
  name         = "mongodb-instance"
  machine_type = "e2-medium"
  zone         = "us-central1-c"

  tags = ["mongo", "http-server", "https-server" ]

  boot_disk {
    initialize_params {
      image = "ubuntu-2204-jammy-v20231030"
      labels = {
        my_label = "ubuntu"
      }
    }
  }


  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }

  service_account {
    email  = "282148687829-compute@developer.gserviceaccount.com"
    scopes = ["cloud-platform"]
  }
}

resource "google_compute_firewall" "default" {
 name    = "mongo-firewall"
 network = "default"

 allow {
   protocol = "icmp"
 }

 allow {
   protocol = "tcp"
   ports    = ["8000"]
 }

 source_ranges = ["0.0.0.0/0"]
 target_tags = ["mongo"]
}

resource "google_cloud_run_v2_service" "default" {
  name     = "fast-api-terraform"
  location = "us-central1"
  ingress = "INGRESS_TRAFFIC_ALL"

  template {
    scaling {
      min_instance_count = 0
      max_instance_count = 1
    }
    timeout = "300s"
    max_instance_request_concurrency = 80
    containers {
      image = "us-east1-docker.pkg.dev/apt-theme-402300/repo-docker/fastapi_image@sha256:13c930a8d6b1126e3765168f908ab44683fa7cdbe7827af357831b64b7cbbe0a"
      resources {
        cpu_idle = true
            limits = {
            memory = "512Mi"
          }
      }
      ports {
        container_port = 8000
      }
    }
    service_account = "brasil-api-cloud-storage@apt-theme-402300.iam.gserviceaccount.com"
  }

}